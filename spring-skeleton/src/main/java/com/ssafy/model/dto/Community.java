package com.ssafy.model.dto;

import java.sql.Date;

public class Community {
	//community 테이블 + community_youtuber_relation 테이블의 컬럼을 합쳐놓은 DTO
	private int cono;
	private String communityName;
	private String communityAgeGroup;
	
	private int yno;					//community_youtuber_relationg 테이블의 컬럼
	private int mentionCount;			//community_youtuber_relationg 테이블의 컬럼
	private Date updateDate;			//community_youtuber_relationg 테이블의 컬럼
	
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
	public int getMentionCount() {
		return mentionCount;
	}
	public void setMentionCount(int mentionCount) {
		this.mentionCount = mentionCount;
	}
	public Date getUpdateDate() {
		return updateDate;
	}
	public void setUpdateDate(Date updateDate) {
		this.updateDate = updateDate;
	}
}