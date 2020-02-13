package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.InterestDao;
import com.ssafy.model.dto.Interest;
import com.ssafy.model.dto.Youtuber;

@Service
public class InterestServiceImpl implements InterestService {
	
	@Autowired
	private InterestDao dao;
	
	@Override
	public List<Integer> search(int usno) {
		try {
			return dao.search(usno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("user가 등록한 관심항목이 있는지 검색 중 에러가 발생했습니다.");
		}
	}

	@Override
	public void insertInterest(Interest interest) {
		try {
			dao.insertInterest(interest);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("user의 관심항목 추가 중 에러가 발생했습니다.");
		}
	}

	@Override
	public void deleteInterest(int usno) {
		try {
			System.out.println("usno" + usno + "삭제할거야");
			dao.deleteInterest(usno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("user의 관심항목 삭제 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Youtuber> searchInterestRecommend(Map<String, Object> condition) {
		try {
			return dao.searchInterestRecommend(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("관심분야에 기반한 유튜버 추천 목록 검색 중 에러가 발생했습니다.");
		}
	}
}