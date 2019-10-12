s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('__names i'.split()))
print('\n'.join(' '.join(s_var_names[i:i+8])for i in range(0, len(s_var_names), 8)) )
