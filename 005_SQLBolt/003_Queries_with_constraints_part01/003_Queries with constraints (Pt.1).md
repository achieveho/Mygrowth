# &lt; SQL Lesson 2: Queries with Constraints (Pt.1) &gt;

---

* 데이터의 개수가 너무 많을 때는, **WHERE** 조건절을 사용해서 필요한 데이터만 보도록 한다.
* **WHERE** 절은 각 데이터 행에 적용되어 특정 열 값을 확인한 후 필터링을 진행한다.
* **WHERE** 절을 잘 사용하면 불필요한 데이터를 얻지 않을 뿐만 아니라, 쿼리 실행 완료 시간도 단축된다.

---

```sql
SELECT column, another_column, ...
FROM mytable
WHERE condition
  AND/OR another_condition
  AND/OR ...;
```

* **AND** 또는 **OR**을 사용하여 더 복잡하고 정교한 조건식을 만들 수 있다.

---

## &lt; 유용한 연산자 모음 &gt;

| Operator | Condition | SQL Example |
| :---: | :--- | :--- |
| `=`, `!=`, `<`, `<=`, `>`, `>=` | Standard numerical operators | col_name **!=** 4 |
| `BETWEEN ... AND ...` | Number is within range of two values (inclusive) | col_name **BETWEEN** 1, 5 **AND** 10 |
| `NOT BETWEEN ... AND ...` | Number is not within range of two values (inclusive) | col_name **NOT BETWEEN** 1 **AND** 10 |
| `IN (...)` | Number exists in a list | col_name **IN** (2, 4, 6) |
| `NOT IN (...)` | Number doesn't exist in a list | col_name **NOT IN** (1, 3, 5) |
