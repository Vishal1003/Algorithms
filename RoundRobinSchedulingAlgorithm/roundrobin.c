#include<stdio.h>
int done(int burst_time[],int len);

int main(){
	printf("-------------------------------------------------------");
	printf("\n****Round Robin Scheduling****\n\n");

	int proc;
	printf("Enter no of processes: ");
	scanf("%d",&proc);
	printf("\n");

	int id[proc];
	int burst_time[proc];
	int burst_time_copy[proc];

	for(int i=0;i<proc;i++){
		printf("Enter the ID of the process: ");
		scanf("%d",&id[i]);

		printf("Enter the burst time: ");
		scanf("%d",&burst_time[i]);
		
		burst_time_copy[i]=burst_time[i];
		printf("\n");
	}

	int quant;
	printf("Enter time quantum: ");
	scanf("%d",&quant);
	printf("\n\n");


	int wait[proc];
	int turn[proc];
	int last[proc];
	for(int i=0;i<proc;i++){
		wait[i]=0;
		turn[i]=0;
		last[i]=0;
	}

	float avg_wait=0;
	float avg_tat=0;
	
	int i=0;
	int time=0;
	while(done(burst_time,proc)!=1){
		if(burst_time[i]!=0){
			if(burst_time[i]>quant){
				burst_time[i]=burst_time[i]-quant;
				wait[i]=wait[i]+time-last[i];
				time=time+quant;
				last[i]=time;
			}
			else{
				wait[i]=wait[i]+time-last[i];
				time=time+burst_time[i];
				burst_time[i]=0;
				turn[i]=time;
			}
		}
		
		i=(i+1)%proc;
	}

	
	printf("Process ID   Burst Time   Waiting Time   Turnaround Time\n");

	for(int i=0;i<proc;i++){
		printf("%d\t\t%d\t\t%d\t\t%d\n",id[i],burst_time_copy[i],wait[i],turn[i]);
	avg_wait = avg_wait + wait[i];
	avg_tat = avg_tat + turn[i];
	}
	
	printf("\n\nThe average waiting time is: %f\n",avg_wait/proc);
	printf("The average turn around time is: %f\n",avg_tat/proc);
}

int done(int burst_time[],int len){
	for(int x=0;x<len;x++){
		if(burst_time[x]!=0)
			return 0;
	}
	return 1;
}