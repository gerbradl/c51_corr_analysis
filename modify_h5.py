
import h5py

def remove_datasets_from_h5(input_filename, output_filename, strings_to_remove):
    def remove_datasets_recursive(group, output_group):
        for key, item in group.items():
            if isinstance(item, h5py.Group):
                output_subgroup = output_group.create_group(key)
                remove_datasets_recursive(item, output_subgroup)
            elif isinstance(item, h5py.Dataset):
                remove_dataset = any(string in key for string in strings_to_remove)
                if not remove_dataset:
                    group.copy(key, output_group)

    with h5py.File(input_filename, 'r') as input_h5, h5py.File(output_filename, 'w') as output_h5:
        remove_datasets_recursive(input_h5, output_h5)

strings_to_remove = ['zP_0', 'zP_1', 'zP_2','zP_3','zP_4' 'zS_0', 'zS_1', 'zS_2', 'zS_3','zS_4', 'log']
remove_datasets_from_h5('scale_setting_seeded.h5', 'scale_setting_final.h5', strings_to_remove)

def add_datasets_to_h5(source_filename, destination_filename):
    with h5py.File(source_filename, 'r') as source_h5, h5py.File(destination_filename, 'a') as destination_h5:
        for ds_name in source_h5:
            source_dataset = source_h5[ds_name]
            destination_h5.copy(source_dataset, ds_name)

# add_datasets_to_h5('scale_setting_seeded_3.h5', 'scale_setting_seeded.h5')
