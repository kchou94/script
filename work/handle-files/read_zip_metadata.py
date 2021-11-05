import zipfile


def meta_info(names):
    with zipfile.ZipFile(names) as z:
        for info in z.infolist():
            print(info.filename)
            if info.create_system == 0:
                system = 'Windows'
            elif info.create_system == 3:
                system = 'Unix'
            else:
                system = 'Unknown'
            print(f'System: {system}')
            print(f'Zip Version: {info.create_version}')
            print('Compression size: ', info.compress_size, 'bytes')
            print("Uncompressed size: ", info.file_size, 'bytes')
            print()


if __name__ == '__main__':
    meta_info('work.zip')
