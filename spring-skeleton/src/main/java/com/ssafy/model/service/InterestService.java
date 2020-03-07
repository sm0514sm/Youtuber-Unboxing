package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Interest;
import com.ssafy.model.dto.Youtuber;

public interface InterestService {
	public List<Integer> search(int usno);
	public void insertInterest(Interest interest);
	public void deleteInterest(int usno);
	public List<Youtuber> searchInterestRecommend(Map<String, Object> condition);
}