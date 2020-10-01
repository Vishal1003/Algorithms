## Kruskal MCST Algorithm:

Alogrithm :

```
Kruskal (V, E)
{
    TE ←Φ
    ∀ v ∈ V make_ set(v)
    Sort E into non decreasing order by weight
    For each edge (u, v) ∈ E taken in non decreasing order
    If find_set(u) ≠ find_set(v)
    {
        TE ←TE∪ {(u ,v)}
        Union (u ,v)
    }
    Return (V, TE)
}
```

Time Complexity : E log(V)
