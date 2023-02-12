try:
    file1 = open('./testfile', 'w')
    file1.write('This is a test file!')
except TypeError:
    print('There was a TypeError!')
except OSError:
    print('There was an OSError')
except:
    print('All other exceptions!')
finally:
    file1.close()
    print('I always run')