package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Growth;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface YoutuberDao {
	public Youtuber search(int yno);
	public List<Youtuber> searchKeyword(String keyword);
	public List<Youtuber> searchAll();
	public List<Youtuber> searchRanking(Map<String, String> condition);
	public List<News> searchNews(int yno);
	public List<Video> searchVideo(int yno);
	public List<Video> searchCommunity(int yno);
	public List<Growth> searchGrowth(int yno);
}
