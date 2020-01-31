package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Growth;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;

public interface YoutuberService {
	public Youtuber search(int yno);
	public List<Youtuber> searchKeyword(String keyword);
	public List<Youtuber> searchAll();
	public List<Youtuber> searchRanking(Map<String, String> condition);
	public List<News> searchNews(int yno);
	public List<Video> searchVideo(int yno);
	public List<Video> searchCommunity(int yno);
	public List<Growth> searchGrowth(int yno);
}