package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Interest;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface InterestDao {
	public int search(int usno);
	public void insertInterest(Interest interest);
	public void deleteInterest(int usno);
	public List<Youtuber> searchInterestRecommend(Map<String, Object> condition);
}
