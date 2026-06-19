# &lt; Queries with constraints (Pt.2) &gt;

---

* **WHERE** 조건 절을 텍스트를 포함해 사용 시,
  * 대소문자를 구분하지 않는 필터링
  * 와일드카드 패턴 일치 여부 확인
* 과 같은 유용한 연산자를 사용할 수 있다.
* 단, 모든 문자열은 ""로 묶어야 SQL의 키워드와 구분할 수 있다.
* 전체 텍스트를 검색할 때는 SQL을 사용하는 것보다 **Apache Lucene** 또는 **Sphinx** 라이브러리를 사용하는 것이 더 좋다.
  * 이 두 라이브러리들은 전체 텍스트를 검색하기 위해 전문적으로 설계된 라이브러리.
  * 국제화 및 고급 쿼리를 포함한 다양하고 효율적인 검색을 지원.

---

## &lt; 텍스트가 포함된 WHERE절 사용에 유용한 연산자 모음 &gt;

| Operator | Condition | Example |
| --- | :--- | :--- |
| `=` | Case sensitive exact string comparison **(notice the single equals)** | col_name = "abc" |
| `!=` or `<>` | Case sensitive exact string inequality comparison | col_name **!=** "abcd" |
| `LIKE` | Case insensitive exact string comparison | col_name **LIKE** "ABC" |
| `NOT LIKE` | Case insensitive exact string inequality comparison | col_name **NOT LIKE** "ABCD" |
| `%` | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name **LIKE** "%AT%" (matches "<u>AT</u>", "<u>AT</u>TIC", "C<u>AT</u>" or even "B<u>AT</u>S") |
| `_` | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) | col_name **LIKE** "AN_" (matches "<u>AN</u>D", but not "<u>AN</u>") |
| `IN (...)` | String exists in a list | col_name **IN** ("A", "B", "C") |
| `NOT IN (...)` | String does not exist in a list | col_name **NOT IN** ("D", "E", "F") |
