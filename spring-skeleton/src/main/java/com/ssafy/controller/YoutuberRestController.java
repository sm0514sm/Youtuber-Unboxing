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

import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Trend;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.YoutuberService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class YoutuberRestController {
	@Autowired
	private YoutuberService youtuberService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("youtuber 고유번호 | youtuber 테이블 조회")
	@GetMapping("/youtuber/{yno}")
	public ResponseEntity<Map<String, Object>> search(@PathVariable int yno){
		Youtuber youtuber = youtuberService.search(yno); 
		return handleSuccess(youtuber);
	}
	
	@ApiOperation("youtuber 고유번호 | youtuber가 속한 카테고리 목록 검색 | 카테고리 번호로 오름차순 정렬")
	@GetMapping("/youtuber/category/{yno}")
	public ResponseEntity<Map<String, Object>> searchCategoryList(@PathVariable int yno){
		List<Category> list = youtuberService.searchCategoryList(yno); 
		return handleSuccess(list);
	}
	
	@ApiOperation("검색 키워드 | youtuber 정보 검색 (채널 이름, 유튜버 이름, 채널 설명에서) | 구독자 순 내림차순 정렬")
	@GetMapping("/youtuber/search/{keyword}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable String keyword){
		List<Youtuber> list = youtuberService.searchKeyword(keyword); 
		return handleSuccess(list);
	}
	
	@ApiOperation("검색 조건 없음 | youtuber 테이블 전체  조회 | 구독자 순 내림차순 정렬")
	@GetMapping("/youtuber/all")
	public ResponseEntity<Map<String, Object>> searchAll(){
		List<Youtuber> list = youtuberService.searchAll(); 
		return handleSuccess(list);
	}
	
	@ApiOperation("정렬 조건, 검색 개수 | youtuber 테이블에서 조건(subscriber,totalViewCount,totalVideoCount,grade,clickCount,updatedDate) 으로 내림차순 정렬 후 num개 만큼 가져옴")
	@GetMapping("/youtuber/rank/{searchCondition}_{num}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable String searchCondition, @PathVariable int num){
		Map<String, String> map = new HashMap<>();
		map.put("searchCondition", searchCondition);
		map.put("num", num + "");
		List<Youtuber> list = youtuberService.searchRanking(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호 | news 테이블에서 해당 youtuber 뉴스 조회 | 기사 날짜 순으로 내림차순 정렬(최신 뉴스 순)")
	@GetMapping("/youtuber/detail/news/{yno}")
	public ResponseEntity<Map<String, Object>> searchNews(@PathVariable int yno){
		List<News> list = youtuberService.searchNews(yno);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호 | youtuber가 올린 영상 조회 | 영상 조회수 순으로 내림차순 정렬")
	@GetMapping("/youtuber/detail/video/{yno}")
	public ResponseEntity<Map<String, Object>> searchVideo(@PathVariable int yno){
		List<Video> list = youtuberService.searchVideo(yno);
		return handleSuccess(list);
	}
	
//	@ApiOperation("youtuber 관련 커뮤니티 조회")
//	@GetMapping("/youtuber/detail/community/{yno}")
//	public ResponseEntity<Map<String, Object>> searchCommunity(@PathVariable int yno){
//		List<Video> list = youtuberService.searchCommunity(yno);
//		return handleSuccess(list);
//	}
	
	@ApiOperation("youtuber 고유번호 | 변화 추이(trend) 테이블 조회 | 기록 일자 순으로 내림차순 정렬(최신순)")
	@GetMapping("/youtuber/detail/trend/{yno}")
	public ResponseEntity<Map<String, Object>> searchTrend(@PathVariable int yno){
		List<Trend> list = youtuberService.searchTrend(yno);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 동영상 개수 | 최근 영상 num개의 정보 및 그 영상의 좋아요 싫어요 비율 정보(goodRatio) | 영상 등록일 순으로 내림차순 정렬(최신순)")
	@GetMapping("/youtuber/detail/charm/video/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchVideoGoodRatio(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		List<Video> list = youtuberService.searchVideoGoodRatio(map);
		return handleSuccess(list);
	}

	@ApiOperation("youtuber 고유번호, 동영상 개수 | 최근 num개 동영상에 대한 좋아요 싫어요 개수 합산 비율 정보(goodRatio) | 총합산비율 하나만 나옴")
	@GetMapping("/youtuber/detail/charm/goodRatio/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchGoodRatio(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		Double list = youtuberService.searchGoodRatio(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 기간(달) | 최근 term 달 간 업로드 한 영상 총 개수")
	@GetMapping("/youtuber/detail/activity/videoCount/{yno}_{term}")
	public ResponseEntity<Map<String, Object>> searchVideoCount(@PathVariable int yno, @PathVariable int term){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("term", term);
		int list = youtuberService.searchVideoCount(map);
		return handleSuccess(list);
	}

	@ApiOperation("youtuber 고유번호, 기간(주) | 주마다 업로드한 영상 개수 (총 term주간) | 영상 등록일 기준 오름차순(과거 등록일부터)")
	@GetMapping("/youtuber/detail/activity/termVideoCount/{yno}_{term}")
	public ResponseEntity<Map<String, Object>> searchTermVideoCount(@PathVariable int yno, @PathVariable int term){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("term", term);
		List<Integer> list = youtuberService.searchTermVideoCount(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 기간(달) | 달마다 커뮤니티에 언급된 횟수 (총 term달간) | 글 날짜 기준 오름차순(과거 등록일부터)")
	@GetMapping("/youtuber/detail/influence/community/{yno}_{term}")
	public ResponseEntity<Map<String, Object>> searchCommunityMentionCount(@PathVariable int yno, @PathVariable int term){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("term", term);
		List<Integer> list = youtuberService.searchCommunityMentionCount(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 기간(달) | 달마다 뉴스에 언급된 횟수 (총 term달간) | 기사 날짜 기준 오름차순(과거 등록일부터)")
	@GetMapping("/youtuber/detail/influence/news/{yno}_{term}")
	public ResponseEntity<Map<String, Object>> searchNewsMentionCount(@PathVariable int yno, @PathVariable int term){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("term", term);
		List<Integer> list = youtuberService.searchNewsMentionCount(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 검색 개수 | 영상들의 조회수 총합의 증감 추이 | 기록 일자 기준 오름차순(과거 등록일부터)")
	@GetMapping("/youtuber/detail/trend/viewCount/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchViewCountDif(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		List<Trend> list = youtuberService.searchViewCountDif(map);
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호, 검색 개수 | 구독자 총합의 증감 추이 | 기록 일자 기준 오름차순(과거 등록일부터)")
	@GetMapping("/youtuber/detail/trend/subscriberCount/{yno}_{num}")
	public ResponseEntity<Map<String, Object>> searchSubscriberCountDif(@PathVariable int yno, @PathVariable int num){
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", yno);
		map.put("num", num);
		List<Trend> list = youtuberService.searchSubscriberCountDif(map);
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