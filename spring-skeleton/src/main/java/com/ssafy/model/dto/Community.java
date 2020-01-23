package com.ssafy.model.dto;

public class Community {
	private int cono;
	private String communityName;
	private String communityAgeGroup;
	private int yno;					//community_youtube_relation에 있는 컬럼
	
	public int getCono() {
		return cono;
	}
	public void setCono(int cono) {
		this.cono = cono;
	}
	public String getCommunityName() {
		return communityName;
	}
	public void setCommunityName(String communityName) {
		this.communityName = communityName;
	}
	public String getCommunityAgeGroup() {
		return communityAgeGroup;
	}
	public void setCommunityAgeGroup(String communityAgeGroup) {
		this.communityAgeGroup = communityAgeGroup;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
}