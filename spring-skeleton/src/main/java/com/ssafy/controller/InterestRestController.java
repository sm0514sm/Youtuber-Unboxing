package com.ssafy.controller;

import java.util.Arrays;
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

import com.ssafy.model.dto.Interest;
import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.InterestService;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;

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
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("user 고유번호, 관심분야 고유번호(,로 구분/최대 3개) | user의 관심항목 추가 또는 업데이트")
	@GetMapping("/interest/insert/{usToken}&{interestList}")
	public ResponseEntity<Map<String, Object>> insertInterest(@PathVariable String usToken, @PathVariable String interestList){
		HashMap<String, Object> userInfo = kakao.getUserInfo(usToken);
    	User user = userService.search(userInfo.get("id").toString());
    	int usno = user.getUsno();
    	
    	int interestNum = interestService.search(usno);
    	System.out.println("interestNum>> " + interestNum);
    	if (interestNum > 0)	//이미 등록된 관심항목이 있다면 삭제한다
    		interestService.deleteInterest(usno);
    	
    	System.out.println("interestNum>> " + interestNum);
    	//관심분야 고유번호, 관심분야 고유번호...
    	String[] itList = interestList.split(",");

    	//삭제한 후, 또는 아예 없었을 때
    	for (int i = 0; i < itList.length; i++) {
    		System.out.println("list " + itList[i]);
			Interest interest = new Interest(usno, Integer.parseInt(itList[i]));
			interestService.insertInterest(interest);
		}
		return handleSuccess("관심분야 추가에 성공했습니다");
	}
	
	
	@ApiOperation("user 고유번호, 관심분야 고유번호(,로 구분/최대 3개) | 관심분야에 기반한 유튜버 추천 목록을 검색 개수만큼 검색 | 같은 관심분야를 즐겨찾기에 추가한 사람이 많은 순서로 내림차순")
	@GetMapping("/interest/search/{usToken}&{interestList}")
	public ResponseEntity<Map<String, Object>> searchInterestRecommend(@PathVariable String usToken, @PathVariable String interestList){
		HashMap<String, Object> userInfo = kakao.getUserInfo(usToken);
    	User user = userService.search(userInfo.get("id").toString());
		
		//관심분야 고유번호, 관심분야 고유번호...
		String[] itList = interestList.split(",");
		
		Map<String, Object> map = new HashMap<>();
		map.put("usno", user.getUsno());
		map.put("interestList", itList);
		
		List<Youtuber> list = interestService.searchInterestRecommend(map);
		return handleSuccess(list);
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