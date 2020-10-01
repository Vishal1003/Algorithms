* Basic example of SAP binary search function for internal tables.
* Not exactly an algorithm, at least not one written by myself, as it is a provided functionality.
* Nevertheless, good to know if tables grow large and the sorting key is not the standard table key.

DATA: ls_likp TYPE likp.
      lt_likp TYPE TABLE OF likp.
      
  SELECT *
    FROM likp
    INTO TABLE @lt_likp
   WHERE erdat = @sy-datum "Or use any other selection criteria
   ORDER BY erzet ASCENDING.
         
"Prerequsit for binary serach: the internal table has to be sorted by the key field in ascending order.
READ TABLE lt_likp WITH KEY erzet = '121212' INTO ls_likp BINARY SEARCH.
