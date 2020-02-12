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

import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.InterestService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class InterestRestController {
	@Autowired
	private InterestService interestService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("user 고유번호, 검색 개수, 관심분야 고유번호(,로 구분/최대 3개) | 관심분야에 기반한 유튜버 추천 목록을 검색 개수만큼 검색 | 같은 관심분야를 즐겨찾기에 추가한 사람이 많은 순서로 내림차순")
	@GetMapping("/interest/search/{usno}&{num}&{interestList}")
	public ResponseEntity<Map<String, Object>> searchInterestRecommend(@PathVariable int usno, @PathVariable int num, @PathVariable String interestList){
		//관심분야 고유번호, 관심분야 고유번호...
		String[] cList = interestList.split(",");
		
		Map<String, Object> map = new HashMap<>();
		map.put("usno", usno);
		map.put("num", num);
		map.put("interestList", cList);
		
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