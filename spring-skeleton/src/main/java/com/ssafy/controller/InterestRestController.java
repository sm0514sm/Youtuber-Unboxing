package com.ssafy.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.ssafy.model.dto.Interest;
import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.InterestService;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;
import com.ssafy.model.service.YoutuberService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class InterestRestController {
	@Autowired
	private InterestService interestService;
	@Autowired
	private KakaoAPI kakao;
	@Autowired
	private UserService userService;
	@Autowired
	private YoutuberService youtuberService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("user 토큰, 관심분야 고유번호(,로 구분/최대 3개) | user의 관심항목 추가 또는 업데이트")
	@GetMapping("/interest/insert/{usToken}&{interestList}")
	public ResponseEntity<Map<String, Object>> insertInterest(@PathVariable String usToken, @PathVariable String interestList){
		HashMap<String, Object> userInfo = userExist(usToken);
    	User user = userService.search(userInfo.get("id").toString());
    	int usno = user.getUsno();
    	
    	int interestNum = interestService.search(usno).size();
    	if (interestNum > 0)	//이미 등록된 관심항목이 있다면 삭제한다
    		interestService.deleteInterest(usno);
    	
    	//관심분야 고유번호, 관심분야 고유번호...
    	String[] itList = interestList.split(",");

    	//삭제한 후, 또는 아예 없었을 때
    	for (int i = 0; i < itList.length; i++) {
			Interest interest = new Interest(usno, Integer.parseInt(itList[i]));
			interestService.insertInterest(interest);
		}
		return handleSuccess("관심분야 추가에 성공했습니다");
	}
	
	@ApiOperation("user 토큰 | user의 관심항목 조회")
	@GetMapping("/interest/search/{usToken}")
	public ResponseEntity<Map<String, Object>> searchInterest(@PathVariable String usToken){
		HashMap<String, Object> userInfo = userExist(usToken);
    	User user = userService.search(userInfo.get("id").toString());
    	int usno = user.getUsno();
    	
    	List<Integer> list = interestService.search(usno);
		return handleSuccess(list);
	}
	
	@ApiOperation("user 토큰, 관심분야 고유번호(,로 구분/최대 3개) | 관심분야에 기반한 유튜버 추천 목록을 검색 개수만큼 검색 | 같은 관심분야를 즐겨찾기에 추가한 사람이 많은 순서로 내림차순 | 추천동영상이 4개보다 적을 경우 영상총조회수가 많은 유튜버들로 나머지를 채움")
	@GetMapping("/interest/search/recommend/{usToken}&{interestList}")
	public ResponseEntity<Map<String, Object>> searchInterestRecommend(@PathVariable String usToken, @PathVariable String interestList){
		HashMap<String, Object> userInfo = userExist(usToken);
    	User user = userService.search(userInfo.get("id").toString());
    	List<Youtuber> list;
    	
    	//관심분야가 아예 없는 경우, 추천동영상 4개 전체를 인기유튜버(총조회수합 기준)로 채움
    	if (interestList == null || interestList.equals("")) {
    		Map<String, String> map = new HashMap<>();
			map.put("searchCondition", "totalViewCount");
			map.put("num", "4");
			list = youtuberService.searchRanking(map);
			
    	} else {
    		//관심분야 고유번호는 ,로 구분되어서(공백없이) String 형태로 들어옴
    		String[] itList = interestList.split(",");
    		
    		Map<String, Object> map = new HashMap<>();
    		map.put("usno", user.getUsno());
    		map.put("interestList", itList);
    		
    		//사용자가 체크한 관심분야를 기준으로 추천동영상을 검색
    		list = interestService.searchInterestRecommend(map);
    		
    		//만약 추천동영상의 개수가 4개 미만이라면, 인기유튜버(총조회수합 기준)로 나머지 빈 자리를 채움
    		if (list.size() < 4) {
    			Map<String, String> map2 = new HashMap<>();
    			map2.put("searchCondition", "totalViewCount");
    			map2.put("num", (4 - list.size()) + "");
    			
    			List<Youtuber> temp = youtuberService.searchRanking(map2);
    			for (Youtuber youtuber : temp)
    				list.add(youtuber);
    		}
    	}
		return handleSuccess(list);
	}
	
	private HashMap<String, Object> userExist(String access_Token) {
		HashMap<String, Object> userInfo = kakao.getUserInfo(access_Token);
		String userID = userInfo.get("id").toString();
		int check = userService.searchUserExist(userID);
		if(check==0) {
			User user = new User();
			if(userInfo.containsKey("email")) {
				String userEmail = userInfo.get("email").toString();
				user.setUserEmail(userEmail);
			}
			String userName = userInfo.get("nickname").toString();
			user.setUserID(userID);
			user.setUserName(userName);
			userService.insertUser(user);
		}
		return userInfo;
	}

	// Exception Handle
	public ResponseEntity<Map<String, Object>> handleFail(Object data, HttpStatus state){
		Map<String, Object> resultMap = new HashMap<String, Object>();
		resultMap.put("state", "fail");
		resultMap.put("data", data);
		return new ResponseEntity<Map<String,Object>>(resultMap, state);
	}
	
	public ResponseEntity<Map<String, Object>> handleSuccess(Object data){
		Map<String, Object> resultMap = new HashMap<String, Object>();
		resultMap.put("state", "ok");
		resultMap.put("data", data);
		return new ResponseEntity<Map<String,Object>>(resultMap, HttpStatus.OK);
	}
}