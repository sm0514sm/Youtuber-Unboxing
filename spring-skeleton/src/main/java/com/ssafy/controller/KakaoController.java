package com.ssafy.controller;

import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.ssafy.model.dto.User;
import com.ssafy.model.service.KakaoAPI;
import com.ssafy.model.service.UserService;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@Controller
public class KakaoController {
	
	@Autowired
    private KakaoAPI kakao;
	@Autowired
	private UserService userService;
	
	@RequestMapping(value="/")
    public String index() {
        
        return "index";
    }
	
	@RequestMapping(value="/login")
    public String login(@RequestParam("code") String code) {
        System.out.println("code:"+code);
    	String access_Token = kakao.getAccessToken(code);
    	System.out.println(access_Token);
    	return "redirect:http://i02a108.p.ssafy.io/?access_Token="+access_Token;
    }
	
}
