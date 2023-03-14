# 디스크 컨트롤러
import heapq


def solution(jobs):
    answer, job_start_time = 0, 0
    num_of_jobs = len(jobs)
    while len(jobs) > 0:
        jobs_arr = []
        for job in jobs:
            if job[0] <= job_start_time:
                heapq.heappush(jobs_arr, [job[1], job[0]])
        if len(jobs_arr) < 1:
            job_start_time += 1
            continue
        min_time_job = heapq.heappop(jobs_arr)
        answer += (job_start_time + min_time_job[0] - min_time_job[1])
        job_start_time += min_time_job[0]
        jobs.remove([min_time_job[1], min_time_job[0]])

    return answer // num_of_jobs
