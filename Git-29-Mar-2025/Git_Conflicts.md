### Understanding `git pull` and local changes

The `git pull` command is essentially a combination of `git fetch` followed by `git merge`. It fetches changes from the remote repository and then attempts to merge them into your current branch. The behaviour of `git pull` regarding local changes depends on whether these local changes conflict with the changes being pulled.

#### Does `git pull` overwrite local changes?

By default, `git pull` does not overwrite unstaged local changes unless there is a conflict between your local changes and the changes coming from the remote repository. If such a conflict exists, Git will not proceed with the merge and will ask you to resolve the conflicts manually.

---

#### Pulling without overwriting local changes

If you wish to fetch and merge remote changes without risking your local changes, you can take the following approach:

> [!IMPORTANT]
> Check what status your git commit branch is in running following command :

```
git status
```

---

> [!INFORMATION]
> **Stash your local changes**:
> Open your Terminal

``` 
git stash
```

---

> [!INFORMATION]
> **Pull the remote changes**:
> In the Terminal
>

```
git fetch origin && git rebase origin/main
```

---

> [!INFORMATION]
> **Reapply your stashed changes**:
> In the Terminal

```
git stash pop
```

After popping the stash, you may need to resolve conflicts between your local changes and the newly pulled changes.

---

> [!IMPORTANT]
> Now you can contained with your push to the github repo

```
git push origin <branch_name>
```

