# Git and GitHub

## Table of contents

1. Basic Commands
2. Merge Conflicts
3. Pull requests
4. Issues
5. Git workflow
6. Commit message convention
7. Good commit

# Git

## Basic Commands

git commands that are most commonly used.

- `git init` Initialize git in your directory
- `rm -rf .git` Remove git from your directory
- `git clone <url>` Clone a remote repository into your local machine
- `git remote add origin <url>` Add remote repository
- `git status` Check the state of files
    - untracked
    - tracked
    - modified
    - unmodified
    - added
    - deleted
    - renamed
- `git add` Add file to track
- `git commit` Commit your changes
    - `git commit -m "your commit message"`
    - `git commit -am "add and commit file"`
    - `git commit -amend` Rewrite your previous commit message
- `git push` Push a file to a remote repository
    - `git push origin main` This says push content to remote name origin branch main
    - `git push -u origin main` Make an upstream to the main branch
- `git pull` Pull the latest commit from a remote repository
- `git branch <branch_name>` Create new branch
    - `git branch -M <new_name>` Rename branch
- `git checkout <branch_name>` Go to another branch
    - `git checkout -b <branch_name>` Create a new branch and checkout to it
- `git merge <branch_name>` Merge 2 branches together
- `git stash` Use to stash your changes so you can check out to another branch without needing to commit your unfinished work
- `git stash pop` Pop out your stash file
- `git squash` Squash the previous commit into one commit using the following commands
    - `git rebase -i HEAD~n`
    - `git merge --squash`
- `git rebase` Merge commit to head of main
- `git branch -d <branch_name>` Delete local branch
- `git push origin --delete <branch_name>` Delete remote branch

## merge conflict

This happens when you merge 2 branches that have changes in the same spot or a file got deleted. To resolve merge conflicts that are in the file you can do 3 ways

![Screen Shot 2565-12-27 at 01.15.33.png](Git%20and%20GitHub%20064db2b7b6e44ba6ba5b5a97abc2ec2f/Screen_Shot_2565-12-27_at_01.15.33.png)

1. Keep all → remove lines 16 18 20
2. Keep up → remove lines 16 18 19 20
3. Keep down → remove lines 16 17 18 20

## Git workflow

- **Centralize workflow**
    
    ![01 Central Repository.svg](Git%20and%20GitHub%20064db2b7b6e44ba6ba5b5a97abc2ec2f/01_Central_Repository.svg)
    
    work only in the main branch 
    
- **Feature branch workflow**
    
    ![07.svg](Git%20and%20GitHub%20064db2b7b6e44ba6ba5b5a97abc2ec2f/07.svg)
    
    developer work in their own branch. when finish with their features their merge back into the main branch
    
- **Gitflow workflow**
    
    ![04 Hotfix branches.svg](Git%20and%20GitHub%20064db2b7b6e44ba6ba5b5a97abc2ec2f/04_Hotfix_branches.svg)
    
- **Forking workflow**

ref: [https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow)

## Commit message convention

```bash
<type>[optional scope]: <description>
```

**Type**

- `fix` → การแก้บัค
- `feat` → การเพิ่ม feature ใหม่
- `docs` → สำหรับการเปลี่ยนแปลงแค่ documentation (ไม่กระทบกับโค้ดหลัก)
- `style` → สำหรับการเปลี่ยนแปลงที่ไม่ได้เปลี่ยนแปลงความหมายของโค้ด เช่น ลบ white-space, การแก้ format, หรือเติม semi-colon ที่หายไป
- `refactor` → สำหรับการแก้ไขที่ไม่ใช่การแก้บัค(fix) หรือ เพิ่มความสามารถใหม่(feature)
- `chore` → การเปลี่ยนแปลงที่ไม่ใช่การแก้บัค(fix)หรือการเพิ่มความสามารถใหม่(feature) เช่น การอัพเดท dependencies
- `test` → เพิ่มส่วนของ test แก้ไขเทสเคสเดิมให้สมบูรณ์ยิ่งขึ้น
- อื่น ๆ → `build` , `ci` , `pref` , `revert`

example:

```bash
feat(home): add button to home page
```

ref: [https://medium.com/scb-techx/เขียน-commit-message-ให้ดียิ่งขึ้นด้วย-conventional-commits-️-3d4f7da1c8ec](https://medium.com/scb-techx/%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%99-commit-message-%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B8%82%E0%B8%B6%E0%B9%89%E0%B8%99%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-conventional-commits-%EF%B8%8F-3d4f7da1c8ec)

## Good commit

> **TLDR**
The Perfect Commit is a single, focused change that should be treated thoughtfully and with care. For things like web applications that can be deployed to production, a commit should be a unit that could be deployed.
> 

A single commit should contains all of the following:

- The **implementation**: a single, focused change
- **Tests** that demonstrate the implementation works
- Updated **documentation** reflecting the change
- A link to an **issue thread** providing further context

ref: [https://simonwillison.net/2022/Oct/29/the-perfect-commit/](https://simonwillison.net/2022/Oct/29/the-perfect-commit/)

# Github

## Pull requests

You open pull request when you want to merge your branch into the main branch. This let people know what changes you make and review them before merging to main

## Issues

You open issues when you see a bug or some feature that can be add into the project