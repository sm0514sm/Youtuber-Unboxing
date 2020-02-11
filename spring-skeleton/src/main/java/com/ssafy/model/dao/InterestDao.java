package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Youtuber;

@Mapper
public interface InterestDao {
	public List<Youtuber> searchInterestRecommend(Map<String, Integer> condition);
}
