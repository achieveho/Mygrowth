# &lt; Filtering and sorting Query results. &gt;

* 테이블 내의 데이터 자체는 고유할 수 있어도, 특정 쿼리의 결과는 그렇지 않을 수 있음.
* DISTINCT 키워드를 사용해 중복된 열 값을 가진 행을 편리하게 제거할 수 있음.

```sql
SELECT DISTINCT col01, col02...
FROM table
WHERE conditions;
```

---

## &lt; ORDER BY &gt;


* 실제 DB에는 데이터가 특정 열과 순서가 없이 추가됨.
  * 그래서 데이터가 많아질수록 쿼리의 결과를 읽고 이해하기가 어려워짐.
* 그래서 ORDER BY 절을 제공함.
  * 지정된 열을 기준으로 오름차순 또는 내림차순으로 결과를 정렬함.
  * 각 행은 지정된 열의 값을 기준으로 영숫자(영문자 + 숫자)순으로 정렬됨.
  * 일부 DB에서는 국제 텍스트가 포함된 데이터를 더 효과적으로 정렬하기 위해 콜레이션을 지정할 수 있음.
* 사용 형식

```sql
SELECT col01, col02...
FROM TABLE

WHERE CONDITIONS
ORDER BY COL ASC/DESC;
```

---

## &lt; (ORDER BY) LIMIT &gt;

* ORDER BY절 아래에 LIMIT과 OFFSET 키워드를 사용할 수 있음.
* LIMIT 키워드
  * 조건에 충족하는 행을 지정한 갯수만큼만 반환함.
* OFFSET 키워드
  * 조건에 충족하는 행들 중 반환할 행의 위치를 지정함.
  * 1부터 시작함.

```sql
SELECT col1, col2...
FROM table
WHERE conditions
ORDER BY column ASC/DESC
LIMIT lim_num OFFSET off_num;
```
