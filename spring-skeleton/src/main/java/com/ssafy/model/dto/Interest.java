package com.ssafy.model.dto;

public class Interest {
	//interest 테이블 + interest_user_relation 테이블의 컬럼을 합쳐놓은 DTO
	private int itno;
	private String itName;
	
	private int usno;		//interest_user_relation 테이블의 컬럼
	
	public Interest(int usno, int itno) {
		this.usno = usno;
		this.itno = itno;
	}
	
	public int getItno() {
		return itno;
	}
	public void setItno(int itno) {
		this.itno = itno;
	}
	public String getItName() {
		return itName;
	}
	public void setItName(String itName) {
		this.itName = itName;
	}
	public int getUsno() {
		return usno;
	}
	public void setUsno(int usno) {
		this.usno = usno;
	}
}