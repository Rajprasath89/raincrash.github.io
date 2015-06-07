---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 05:35:00+00:00
layout: post
slug: reset-the-password-of-mysql-in-linux
title: Reset the Password of MySQL in Linux
wordpress_id: 150
---

If you had forgot the password of MySQl in your Linux System, you can always reset it. Usually, you would get the **1025 (28000)** **error message** if you entered a wrong password or forgot to enter one.

  
`**ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)**`  
  
The following steps will help you to change you password. Use need to login as root (superuser) to do this.  
  


  * Stop the MySQl server from running. Use the Following code:  
`**# service mysql stop **`

  * Open the mysql startup script. Add -skip-grant-tables to it.  Now lets start up the mysql daemon and skip the grant tables which store the passwords.
      **  mysqld_safe --skip-grant-tables **  


  * ** **You should see mysqld start up successfully. Now you should be able to connect to mysql without a  password.   
**       mysql --user=root mysql**

**       ****update user set Password=PASSWORD('new-password') where user='root';  
       flush privileges;  
       exit;**

  * Now, restart your MySQl with the new password. It works!
