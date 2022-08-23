class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots

    def get_config(self):
        config = ['Материнская плата: ' + self.name,
                  'Центральный процессор: ' + self.cpu.name + ', ' + str(self.cpu.fr),
                  'Слотов памяти: ' + str(self.total_mem_slots),
                  ]
        temp_list = []
        for i in self.mem_slots:
            temp_list.append(i.name + '-' + str(i.volume))
        config.append('Память: ' + ";".join(map(str, temp_list)))
        return config


cpu = CPU('Intel', 2666)
memory_1 = Memory('Crucial', 4096)
memory_2 = Memory('Samsung', 4096)
mb = MotherBoard('HP', cpu, [memory_1, memory_2])
print(mb.get_config())
