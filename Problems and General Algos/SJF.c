#include <stdio.h>

int main()
{
    printf("\t***Priority Scheduling***\n\n");
    int jobs;
    printf("Enter no of jobs:");
    scanf("%d",&jobs);
    printf("\n");

    int p[jobs];
    int p_num[jobs];
    int j_num[jobs];
    for(int i=0;i<jobs;i++){
        printf("Enter burst time of Process %d:",i+1);
        scanf("%d",&p[i]);

        printf("Enter Priority of Process %d:",i+1);
        scanf("%d",&p_num[i]);

        j_num[i] = i+1;
        printf("\n");
    }

    for(int i=0;i<jobs;i++){
        int small = p_num[i];
        int pos = i;
        for(int j=i+1;j<jobs;j++){
            if(small>p_num[j])
            {
                small = p_num[j];
                pos = j;
            }
        }

        int temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;

        temp = p_num[i];
        p_num[i] = p_num[pos];
        p_num[pos] = temp;

        temp = j_num[i];
        j_num[i] = j_num[pos];
        j_num[pos] = temp;
    }

    printf("Job Priority  Burst Time  Waiting Time  Turnaround Time\n");
    int wait = 0;
    int turn = p[0];

    float waitSum = 0;
    float turnSum = 0;

    for(int i=0;i<jobs;i++){

       waitSum+=wait;
       turnSum+=turn;
        printf("%d\t%d\t%d\t\t%d\t\t%d\n",j_num[i],p_num[i],p[i],wait,turn);
        wait+=p[i];
        turn+=p[i+1];
    }

    waitSum = waitSum/jobs;
    turnSum = turnSum/jobs;

    printf("\nAverage Waiting Time is %f",waitSum);
    printf("\nAverage Turnaround Time is %f\n",turnSum);

    printf("\n\t***Priority Scheduling***\n");
    return 0;
}
