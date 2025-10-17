# Pandas трюк: ускоряем группировки с map вместо merge_groupby

Когда нужно добавить агрегированные значения (например, среднее по группе) обратно в исходный DataFrame, большинство разработчиков делают `groupby().transform()` или `merge()`.  
Но есть менее известный способ — использовать `map()` после `groupby().mean()`, который в некоторых случаях работает в 2–3 раза быстрее и требует меньше памяти.

Фокус в том, что `groupby().mean()` создаёт компактный Series, где индекс — это категория, а значения — результат агрегации.  
А `map()` просто подставляет их обратно в исходный DataFrame без тяжёлого join.

```python
import pandas as pd
import numpy as np

# пример данных
N = 5_000_000
df = pd.DataFrame({
    "group": np.random.choice(["A", "B", "C", "D"], N),
    "value": np.random.randn(N)
})

# классический подход
df["mean_value_merge"] = df["group"].map(df.groupby("group")["value"].mean())

# сравнение с transform
df["mean_value_transform"] = df.groupby("group")["value"].transform("mean")

# идентичность результата
print(df["mean_value_merge"].equals(df["mean_value_transform"]))
```

Это особенно полезно на миллионах строк, когда transform начинает "проседать".  
Метод даёт тот же результат, но заметно экономнее по CPU и RAM.