# list_spase = {'global': {'val': [], 'parent': 'None'}}
#
#
# def create_name_spase(spase, parent):
#     list_spase[spase] = {'val': [], 'parent': parent}
#     return list_spase
#
#
# def add_val_spase(val, spase):
#     list_spase[spase]['val'].append(val)
#     return list_spase
#
#
# def get_parent_val(spase, val):
#     if spase in list_spase:
#         if val in list_spase[spase]['val'] and spase == 'global':
#             print(spase)
#             return
#         elif val not in list_spase[spase]['val'] and spase == 'global':
#             print(list_spase[spase]['parent'])
#             return
#         elif val in list_spase[spase]['val']:
#             print(spase)
#             return
#         else:
#             get_parent_val(list_spase[spase]['parent'], val)
#             return
#     else:
#         if val in list_spase['global']['val']:
#             print('global')
#         else:
#             print('None')
#
# for i in range(int(input())):
#     command, spase, val_parent = input().split()
#     if command == 'add':
#         add_val_spase(val_parent, spase)
#     elif command == 'create':
#         create_name_spase(spase, val_parent)
#     elif command == 'get':
#         get_parent_val(spase, val_parent)
#
#
# print(list_spase)
#
#
# n = int(input())
#
# parent = {"global": None}
# vs = {"global": set()}
#
# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)