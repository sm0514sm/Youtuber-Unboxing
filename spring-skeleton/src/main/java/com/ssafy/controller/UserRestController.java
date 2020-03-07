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
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class UserRestController {
	@Autowired
	private UserService userService;
	@Autowired
	private KakaoAPI kakao;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
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
	
	@ApiOperation("usToken | usToken을 이용한 회원정보 조회")
	@GetMapping("/user/search/{usToken}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable String usToken){
		HashMap<String, Object> userInfo = userExist(usToken);
    	User user = userService.search(userInfo.get("id").toString());
		return handleSuccess(user);
	}
	
	
	@ApiOperation("userID | 해당 user가 즐겨찾기 한 youtuber 목록 검색")
	@GetMapping("/user/favorite/{userID}")
	public ResponseEntity<Map<String, Object>> searchUserFavoriteYoutuber(@PathVariable String userID){
		List<Youtuber> list = userService.searchUserFavoriteYoutuber(userID); 
		return handleSuccess(list);
	}

	@ApiOperation("userID | 해당 userID의 회원 가입 여부 조회 | 있으면 1 없으면 0")
	@GetMapping("/user/exist/{userID}")
	public ResponseEntity<Map<String, Object>> searchUserExist(@PathVariable String userID){
		int userCount = userService.searchUserExist(userID); 
		return handleSuccess(userCount);
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