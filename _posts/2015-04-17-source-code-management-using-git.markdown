---
author: sricharanchiruvolu
comments: true
date: 2015-04-17 15:27:41+00:00
layout: post
slug: source-code-management-using-git
title: Source code management using GIT
wordpress_id: 198
disqus: y
---

<blockquote>Here's my article for Sanchita-15 (Amrita School of Engineering - Annual Magazine).</blockquote>



Git is a distributed revision control and source code management system.  It was developed by Linus Torvalds, the father of Linux kernel. It is designed to handle everything from small to very large software projects with speed and efficiency. Projects that use git for their source code management include Linux Kernel, Android, Debian, GNOME, Ruby on Rails, VLC, e.t.c.

**** ****

Software projects require collaboration of code. Software developers need to work simultaneously without overwriting each other’s changes as well as maintain a history of every version of software they release. This is where a version control system like git comes into picture. So, What is a version control system? It’s a software that helps software developers to work together and maintain a complete history of their work. A version control system allows you to track the history of a collection of files and includes the functionality to revert the collection of files to another version. Each version captures a snapshot of the files at a certain point in time. The collection of files is usually _source code_ for a programming language but a typical version control system can put any type of file under version control.

**** ****

In a Distributed version control systems, DVCS (such as Git, Mercurial, Bazaar or Darcs), clients don’t just check out the latest snapshot of the files: they fully mirror the repository. Thus if any server dies, and these systems were collaborating via it, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

**** ****

As most of the operations are performed locally, it gives a huge benefit in terms of speed. Git does not rely on the central server; that is why, there is no need to interact with the remote server for every operation. The core part of Git is written in C, which avoids runtime overheads associated with other high-level languages. Though Git mirrors entire repository, the size of the data on the client side is small. This illustrates the efficiency of Git.

**** ****

Furthermore, many of these systems deal pretty well with having several remote repositories they can work with, so you can collaborate with different groups of people in different ways simultaneously within the same project. This allows you to set up several types of workflows that aren’t possible in centralized systems, such as hierarchical models.

Before we dive further into version controlling our software projects, let’s look at some terms associated with GIT.

_Repository _- The collection of files including the storage of their revision history.

_Commit_ - A commit is an object of change done on the repository. It identifies a new revision of the content of the repository. Each commit object contains the author and the committer, thus making it possible to identify who did the change.

_Branch_ - A pointer to a commit. If you’re working on a certain branch, the creation of new commit advances this pointer to the newly created commit.

Git allows the user to synchronize the local repository with other (remote) repositories.

Users with sufficient authorization can _push_ changes from their local repository to remote repositories. They can also _fetch_ or _pull _changes from other repositories to their local Git repository.

Now that we understand what GIT is, let’s start using GIT in our own software projects

**SETUP GIT**

Different releases of GIT can be downloaded from [http://git-scm.com/download/](http://git-scm.com/download/) for Windows, Mac OS X, Linux and Solaris. The installation process is as usual. Alternatively, there are various GUI clients available that helps you to manage you git repos efficiently. GitHub has many features including, GUI clients for each platform, hosts your static web repositories e.t.c.

**CREATE A NEW REPOSITORY**

Create a new directory (New Folder), say ‘random_name’. Open it and perform a ‘git init’ to create a new repository.

**CHECKOUT A REPOSITORY**

Create a working copy of a local repository by running the command ‘git clone /path/to/repository/’ when using a remote server, your command will be ‘git clone username@host:/path/to/repository/’.

**WORKFLOW**

Your local repository consists of three ‘trees’ maintained by git. The first one is your ‘Working Directory’ (say, random_name) which holds the actual files. The second one is call the ‘Index’ which acts as a staging area and finally the ‘HEAD’ which points to the last commit you’ve made.

**ADD AND COMMIT**

You can propose changes (add it to the Index) using ‘git add <filename>’ of ‘git add *’ (To add all the files).This is the first step in the basic git workflow. To actually commit these changes use, ‘git commit -m ”commit_message”’.Now the file is committed to the HEAD, but not in your remote repository yet.

**PUSHING CHANGES**

If you have not cloned an existing repository and want to connect your repository to a remote server, you need to add it with, ‘git remote add origin <server>’. Now, you will be able to push your changes to the selected remote server, namely ‘master’.

You are now in the HEAD of your local working copy. To send those changes to your remote repository, execute ‘git push origin master’. Change ’master’ to whatever branch you want to push changes to.

**UPDATE AND MERGE**

To update your local repository to the newest commit, execute ‘git pull’ in your working directory to fetch and merge remote changes. To merge another branch into your active branch (e.g. master), use ‘git merge <branch>’. In both cases git tries to auto-merge changes. Unfortunately, this is not always possible and results in conflicts. You should now merge these conflicts manually. After changing the files shown by the git, you need to mark them as merged with ‘git add <filename>’. Before merging changes, you can preview them using ‘git diff <source_branch> <target_branch>’.



<blockquote>Now, you should feel comfortable using Git and you can do all the basic local Git operations – creating or cloning a repository, making changes, staging and committing those changes, and viewing the history of all the changes the repository has been through. Feel free to use it in your software projects.</blockquote>
