package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Youtuber;

public interface InterestService {
	public List<Youtuber> searchInterestRecommend(Map<String, Integer> condition);
}