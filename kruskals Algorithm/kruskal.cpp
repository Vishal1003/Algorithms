#include <bits/stdc++.h>
using namespace std;
#define REP(i, a, b) for (int i = a; i < b; i++)
#define vi vector<int>
#define vvi vector<vi>
#define pushb push_back
#define miN map<int, struct Node *>

void inputEdges(vvi &arr, int n);

typedef struct Node
{
    struct Node *next;
} Node;

void initDic(miN &dic, int V)
{
    int index = 1;
    while (V--)
    {
        Node *newNode = new Node;
        newNode->next = NULL;
        dic[index] = newNode;
        index++;
    }
}

Node *find(miN dic, int ele) // Return parentSet of the element Node
{
    Node *p = dic[ele];
    while (p->next != NULL)
    {
        p = p->next;
    }
    return p;
}

void unionOp(miN dic, int u, int v)
{
    Node *src = dic[u];
    Node *des = dic[v];
    int mini = min(u, v);
    if (mini == u)
    { // u is parent of v
        src->next = des;
    }
    else
    { // v is parent of u
        des->next = src;
    }
}

int main()
{
    int V, E;
    cout << "\nENTER NUMBER OF VERTICES (V)  : ";
    cin >> V;
    miN dic;
    initDic(dic, V);

    cout << "\nENTER NUMBER OF EDGES (E) :";
    cin >> E;
    vvi mapper;
    inputEdges(mapper, E);
    sort(mapper.begin(), mapper.end());

    int i;
    int count = 0;
    int cost = 0;
    REP(i, 0, E)
    {
        if (count == V - 1)
            break;
        Node *sourceSet = find(dic, mapper[i][1]); // Returns Set to which u belongs
        Node *destSet = find(dic, mapper[i][2]);   // Returns set to which v belongs

        if (sourceSet != destSet)
        {                                             // no cycle formed if sets are different add cost to solution
            unionOp(dic, mapper[i][1], mapper[i][2]); // Perform Union Operation
            cost += mapper[i][0];
            count++;
        }
    }

    cout << cost;

    return 0;
}

void inputEdges(vvi &arr, int n)
{
    while (n--)
    {
        int weight, u, v;
        cout << "ENTER : SOURCE DESTINATION WEIGHT (nodes will be between [1..V]:)" << endl;
        cin >> u >> v >> weight;
        arr.push_back({weight, u, v});
    }
}