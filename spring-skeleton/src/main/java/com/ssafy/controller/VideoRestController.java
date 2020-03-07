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

import com.ssafy.model.dto.Video;
import com.ssafy.model.service.VideoService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class VideoRestController {
	@Autowired
	private VideoService videoService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("video 고유번호 | video 정보 검색")
	@GetMapping("/video/{vno}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable int vno){
		Video video = videoService.search(vno); 
		return handleSuccess(video);
	}
	
	@ApiOperation("keyword | video 이름,설명,태그 키워드가 포함된 video 목록 검색 | 영상조회수 기준 내림차순")
	@GetMapping("/video/search/{keyword}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable String keyword){
		List<Video> list = videoService.searchKeyword(keyword); 
		return handleSuccess(list);
	}
	
	@ApiOperation("전체 video 목록 조회 | 영상조회수 기준 내림차순")
	@GetMapping("/video/all")
	public ResponseEntity<Map<String, Object>> searchAll(){
		List<Video> list = videoService.searchAll(); 
		return handleSuccess(list);
	}
	
	@ApiOperation("정렬 조건, 검색 개수 | 정렬 조건(videoViewCount, videoCommentCount, good, bad, regDate)으로 정렬 후 검색 개수만큼 가져옴 | 정렬 기준으로 내림차순\n정렬 조건이 잘못 입력된 경우 아무것도 반환하지 않음")
	@GetMapping("/video/rank/{searchCondition}_{num}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable String searchCondition, @PathVariable int num){
		Map<String, String> map = new HashMap<>();
		map.put("searchCondition", searchCondition);
		map.put("num", num + "");
		List<Video> list = videoService.searchRanking(map);
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