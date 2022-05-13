fst_name = " larry   "
lst_name = "   holedigger  "
full_name = f"{fst_name} {lst_name}"

print (full_name)

rstrip = full_name.rstrip()
print(rstrip)

lstrip = full_name.lstrip()
print(lstrip)

strip = full_name.strip()
print(strip)

fst_name_strip = fst_name.strip()
lst_name_strip = lst_name.strip()
full_name_strip = f"{fst_name_strip} {lst_name_strip}"
print(full_name_strip.title())

''' It appears that you need to strip raw data,
and not operating on 'f' (full_name in this case).'''