---
author: sricharanchiruvolu
comments: true
date: 2013-12-31 10:00:00+00:00
layout: post
slug: write-ups-for-cryptography-challenges-from-enigmagroup
title: Write-ups For Cryptography Challenges from EnigmaGroup
wordpress_id: 153
---

**Challenge 1**:  
  
> EbGguvEgrRavfNcvRprbsShpXvatCvFf   
  
This is ROT13 Ceaser cipher. It can be easily identified as it is a continuous string with capital and smaller alphabets without any numericals.  
  
**Challenge 2:**  
 
> VGhpcyBvbmUgd2FzIGJhc2U2NC4gSXQncyBhIGxpdHRsZSBoYXJkZXIgdGhhbiB0aGUgcHJldmlvdXMgbWlzc2lvbi4gVGhlID09IG9wZXJhdG9ycyBnaXZlIGJhc2U2NCBhd2F5Lg==  
  


This one was base64. It's a little harder than the previous mission. The == operators give base64 away.

  


**Challenge 3:**  
 
> e515fd7ac3432a1392295e3180bb1ed1  
 
This is a MD5 hash.The MD5 message-digest algorithm is a widely used cryptographic hash function producing a 128-bit (16-byte) hash value, typically expressed in text format as a 32 digit hexadecimal number. MD5 has been utilized in a wide variety of cryptographic applications, and is also commonly used to verify data integrity.  
  
**Challenge 4:**  
 
> fe6bc60ffe1523e3fea5223a5b562e7be476ff21  
  
This is SHA-1. SHA-1 produces a 160-bit (20-byte) hash value. A SHA-1 hash value is typically expressed as a hexadecimal number, 40 digits long.SHA stands for "secure hash algorithm". The four SHA algorithms are structured differently and are distinguished as SHA-0, SHA-1, SHA-2, and SHA-3. SHA-1 is very similar to SHA-0, but corrects an error in the original SHA hash specification that led to significant weaknesses. The SHA-0 algorithm was not adopted by many applications. SHA-2 on the other hand significantly differs from the SHA-1 hash function
