
## Git Clone and Git Pull

**Step 1: Open your terminal**

* On Mac or Linux, you can use Spotlight to find Terminal. Click on Spotlight, type "Terminal", and press Enter.
* On Windows, you can search for "Git Bash" (or "Command Prompt") in the Start menu.

---

**Step 2: Navigate to your project directory**

* Type `cd` followed by the path to your project directory. For example:
```
cd ~/Projects/
```
Replace `~/Projects/` with the actual path to your project directory where you want to clone the repository.

---

**Step 3: Clone the GitHub repository**

* Type the following command and press Enter:
```
git clone https://github.com/SentinelMurphy/AI-Development.git
```
This will download a copy of the repository from GitHub to your local machine.

---

**Step 4: Change into the cloned repository directory**

* Type `cd AI-Development/` and press Enter. This will take you into the directory where the repository is stored.

---

**Step 5: Pull changes from the main branch**

* Type the following command and press Enter:
```
git pull origin main
```
This will fetch changes from the remote `main` branch and merge them into your local `main` branch.

That's it! You've successfully pulled changes from the GitHub repository. If you want to verify that the changes were pulled, you can use:

```
git status
```


**What's happening:**

* `git pull` tells Git to fetch changes from the remote repository.
* `origin` specifies the name of the remote repository (in this case, your own repository).
* `branch_name` specifies which branch you want to pull changes from.

**Tips and Variations:**

* If you're not sure what branch you should pull from, use `git status` to check the current branch.
* If you want to pull changes from a specific commit or tag, use `git pull origin branch_name@commit_hash`.
* If you want to pull changes from all branches (not recommended), use `git pull --all`.
