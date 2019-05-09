package com.churchill.api.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data 
@NoArgsConstructor
public class Post {
	
	@Id
	@GeneratedValue
	private Long id;
	private String message;
	private String author;
	
	public Post (String author, String msg) {
		this.author = author;
		this.message = msg;
	}

}


