import sys


class CopyFile:
    def __init__(self):
        self.db_data = [
            {'id': 1, 'name': 'root', 'parent_id': None},
            {'id': 2, 'name': 'two', 'parent_id': 1},
            {'id': 3, 'name': 'three', 'parent_id': 2},
            {'id': 4, 'name': 'four', 'parent_id': 2},
        ]
        self.max_id = max([x['id'] for x in self.db_data])

    def load_all(self):
        """ 模拟查询出库中所有数据 """
        return self.db_data

    def save(self, name, parent_id):
        """ 插入数据返回自增ID """
        self.max_id += 1
        self.db_data.append({
            'id': self.max_id, 'name': name, 'parent_id': parent_id
        })
        return self.max_id

    def copy_file(self, file_id, parent_id):
        """ 在此实现复制方法 """
        if self.db_data[file_id-1]['id'] == file_id and self.db_data[file_id-1]['parent_id'] == parent_id:
            self.save(self.db_data[file_id-1]['name'], self.db_data[file_id-1]['parent_id'])#先将父文件插入db_data
            for x in range(self.max_id):
                if self.db_data[self.max_id - 1]['parent_id'] == 1:
                    father_id = self.max_id
                if self.db_data[x]['parent_id'] == file_id:
                    self.save(self.db_data[x]['name'], father_id)
        else:
            print('file_id is not exist')
            sys.exit(0)


if __name__ == '__main__':
    copy_file = CopyFile()
    copy_file.copy_file(1, )
    print(copy_file.load_all())


