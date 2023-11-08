class Job:
    def _init_(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)

        slot = [-1] * (maxi + 1)
        scheduled_jobs = []
        countJobs = 0
        jobProfit = 0

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    scheduled_jobs.append(jobs[i].id)
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break

        return countJobs, jobProfit, scheduled_jobs

if __name__ == "__main__":
    num_jobs = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(num_jobs):
        id = int(input(f"Enter the ID of job {i + 1}: "))
        deadline = int(input(f"Enter the deadline of job {i + 1}: "))
        profit = int(input(f"Enter the profit of job {i + 1}: "))
        jobs.append(Job(id, deadline, profit))

    count, profit, scheduled_jobs = Solution().jobScheduling(jobs)
    print("Maximum number of jobs and their total profit:")
    print(count, profit)
    print("Scheduled job IDs:", scheduled_jobs)