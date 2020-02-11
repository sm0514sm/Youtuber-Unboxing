package com.ssafy.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.ssafy.model.dto.Favorite;
import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;
import com.ssafy.model.service.FavoriteService;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;

import io.swagger.annotations.ApiOperation;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class FavoriteRestController {
	@Autowired
	private FavoriteService favoriteService;
	@Autowired
	private KakaoAPI kakao;
	@Autowired
	private UserService userService;
	
	@ExceptionHandler
	public ResponseEntity<Map<String, Object>> handle(Exception e){
		return handleFail(e.getMessage(), HttpStatus.OK);
	}
	
	@ApiOperation("해당 youtuber를 해당 user의 즐겨찾기에 추가")
	@PostMapping("/favorite/insert")
	public ResponseEntity<Map<String, Object>> insertFavorite(@RequestParam Map<String, Object> fav){
		Gson gson = new Gson(); 
		String json = gson.toJson(fav); 
    	JsonParser parser = new JsonParser();
    	JsonElement element = parser.parse(json);
    	
    	HashMap<String, Object> userInfo = kakao.getUserInfo(element.getAsJsonObject().get("token").getAsString());
    	User user = userService.search(userInfo.get("id").toString());
		Favorite favorite = new Favorite();
		favorite.setUsno(user.getUsno());
		favorite.setYno(element.getAsJsonObject().get("yno").getAsInt());
		
		favoriteService.insertFavorite(favorite);
		return handleSuccess("즐겨찾기 등록 완료");
	}
	
	@ApiOperation("youtuber 고유번호, user 고유번호 | 해당 youtuber를 해당 user의 즐겨찾기에서 삭제")
	@DeleteMapping("/favorite/delete/{yno}&{usno}")
	public ResponseEntity<Map<String, Object>> searchKeyword(@PathVariable String yno,  @PathVariable String usno){
		System.out.println(yno);
		System.out.println(usno);
		HashMap<String, Object> userInfo = kakao.getUserInfo(usno.toString());
    	User user = userService.search(userInfo.get("id").toString());
		
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", Integer.parseInt(yno));
		map.put("usno", user.getUsno());
		System.out.println("yno: "+yno);
		System.out.println("usno: "+user.getUsno());
		favoriteService.deleteFavorite(map); 
		return handleSuccess("즐겨찾기 삭제 완료");
	}
	
	@ApiOperation("youtuber 고유번호, user 고유번호 | 해당 user의 즐겨찾기에 해당 youtuber가 있는지 조회 (있으면 1, 없으면 0)")
	@GetMapping("/favorite/select/{yno}&{usno}")
	public ResponseEntity<Map<String, Object>> searchFavorite(@PathVariable String yno, @PathVariable String usno){
		System.out.println(yno);
		System.out.println(usno);
		HashMap<String, Object> userInfo = kakao.getUserInfo(usno.toString());
    	User user = userService.search(userInfo.get("id").toString());
		
		Map<String, Integer> map = new HashMap<>();
		map.put("yno", Integer.parseInt(yno));
		map.put("usno", user.getUsno());
		System.out.println("yno: "+yno);
		System.out.println("usno: "+user.getUsno());
		int count = favoriteService.searchFavorite(map);
		return handleSuccess(count);
	}
	
	@ApiOperation("user 고유번호 | 해당 user가 즐겨찾기 한  youtuber 목록 검색 | 즐겨찾기 추가 날짜 기준 내림차순")
	@GetMapping("/favorite/user/{usno}")
	public ResponseEntity<Map<String, Object>> searchUserFavoriteYoutuber(@PathVariable String usno){
		System.out.println(usno);
		HashMap<String, Object> userInfo = kakao.getUserInfo(usno.toString());
    	User user = userService.search(userInfo.get("id").toString());
		List<Youtuber> list = favoriteService.searchUserFavoriteYoutuber(user.getUsno()); 
		return handleSuccess(list);
	}
	
	@ApiOperation("youtuber 고유번호 | 해당 youtuber 즐겨찾기 한 user 수 총합 조회")
	@GetMapping("/favorite/youtuber/{yno}")
	public ResponseEntity<Map<String, Object>> searchRanking(@PathVariable int yno){
		int count = favoriteService.searchYoutuberFavoriteNum(yno);
		return handleSuccess(count);
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