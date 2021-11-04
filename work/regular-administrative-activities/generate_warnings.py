import warnings

warnings.simplefilter(action='error', category=UserWarning)
print('Before')
warnings.warn('This is a warning')
print('After')
