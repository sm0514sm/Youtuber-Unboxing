package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.InterestDao;
import com.ssafy.model.dto.Youtuber;

@Service
public class InterestServiceImpl implements InterestService {
	
	@Autowired
	private InterestDao dao;

	@Override
	public List<Youtuber> searchInterestRecommend(Map<String, Integer> condition) {
		try {
			return dao.searchInterestRecommend(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("관심분야에 기반한 유튜버 추천 목록 검색 중 에러가 발생했습니다.");
		}
	}
}