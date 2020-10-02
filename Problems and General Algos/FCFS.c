#include <stdio.h>

int main()
{

    printf("\t***Shortest Job First***\n\n");
    int jobs;
    printf("Enter no of jobs:");
    scanf("%d",&jobs);

    int p[jobs];
    int p_num[jobs];
    for(int i=0;i<jobs;i++){
        printf("Enter burst time of Process %d:",i+1);
        scanf("%d",&p[i]);
        p_num[i] = i+1;
    }
    printf("\n");

    for(int i=0;i<jobs;i++){
        int small = p[i];
        int pos = i;
        for(int j=i+1;j<jobs;j++){
            if(small>p[j])
            {
                small = p[j];
                pos = j;
            }
        }

        int temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;

        temp = p_num[i];
        p_num[i] = p_num[pos];
        p_num[pos] = temp;
    }

    printf("Job\tBurst Time\tWaiting Time\tTurnaround Time\n");
    int wait = 0;
    int turn = p[0];

    float waitSum = 0;
    float turnSum = 0;

    for(int i=0;i<jobs;i++){
        waitSum+=wait;
        turnSum+=turn;

        printf("%d\t  %d\t\t    %d\t\t    %d\n",p_num[i],p[i],wait,turn);
        wait+=p[i];
        turn+=p[i+1];
    }


    waitSum = waitSum/jobs;
    turnSum = turnSum/jobs;
    printf("\nAverage Waiting Time: %f\n",waitSum);
    printf("Average Turnaround Time: %f\n",turnSum);

    printf("\n\t***Shortest Job First***\n");
    return 0;
}
