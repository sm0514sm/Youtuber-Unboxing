package com.ssafy.model.dto;

import java.sql.Date;

public class Video {
	private int vno;
	private int yno;
	private String videoName;
	private String videoDescription;
	private int videoViewCount;
	private int videoCommentCount;
	private int good;
	private int bad;
	private Date retDate;
	
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
}