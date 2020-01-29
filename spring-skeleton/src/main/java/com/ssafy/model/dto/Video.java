package com.ssafy.model.dto;

import java.sql.Date;

public class Video {
	//vidio 테이블 + youtube_category 테이블의 컬럼을 합쳐놓은 DTO
	
	private int vno;
	private int yno;
	private String videoName;
	private String videoDescription;
	private int videoViewCount;
	private int videoCommentCount;
	private int good;
	private int bad;
	private Date retDate;
	private int ycano;
	private String tags;
	private String thumbnail;
	private String topic;
	
	private String krCategory;	//youtube_category 테이블의 컬럼
	private String enCategory;	//youtube_category 테이블의 컬럼
	
	public int getVno() {
		return vno;
	}
	public void setVno(int vno) {
		this.vno = vno;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
	public String getVideoName() {
		return videoName;
	}
	public void setVideoName(String videoName) {
		this.videoName = videoName;
	}
	public String getVideoDescription() {
		return videoDescription;
	}
	public void setVideoDescription(String videoDescription) {
		this.videoDescription = videoDescription;
	}
	public int getVideoViewCount() {
		return videoViewCount;
	}
	public void setVideoViewCount(int videoViewCount) {
		this.videoViewCount = videoViewCount;
	}
	public int getVideoCommentCount() {
		return videoCommentCount;
	}
	public void setVideoCommentCount(int videoCommentCount) {
		this.videoCommentCount = videoCommentCount;
	}
	public int getGood() {
		return good;
	}
	public void setGood(int good) {
		this.good = good;
	}
	public int getBad() {
		return bad;
	}
	public void setBad(int bad) {
		this.bad = bad;
	}
	public Date getRetDate() {
		return retDate;
	}
	public void setRetDate(Date retDate) {
		this.retDate = retDate;
	}
	public int getYcano() {
		return ycano;
	}
	public void setYcano(int ycano) {
		this.ycano = ycano;
	}
	public String getTags() {
		return tags;
	}
	public void setTags(String tags) {
		this.tags = tags;
	}
	public String getThumbnail() {
		return thumbnail;
	}
	public void setThumbnail(String thumbnail) {
		this.thumbnail = thumbnail;
	}
	public String getTopic() {
		return topic;
	}
	public void setTopic(String topic) {
		this.topic = topic;
	}
	public String getKrCategory() {
		return krCategory;
	}
	public void setKrCategory(String krCategory) {
		this.krCategory = krCategory;
	}
	public String getEnCategory() {
		return enCategory;
	}
	public void setEnCategory(String enCategory) {
		this.enCategory = enCategory;
	}
}