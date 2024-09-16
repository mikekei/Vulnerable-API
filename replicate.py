import yaml

def generate_replicas(swagger_path, output_path, num_replicas=500):
    # Load the original swagger file
    with open(swagger_path, 'r') as file:
        swagger_data = yaml.safe_load(file)

    # Collect paths to replicate
    original_paths = swagger_data.get('paths', {})
    
    new_paths = {}

    # Replicate each path num_replicas times
    for path, details in original_paths.items():
        for i in range(num_replicas):
            new_path = f"{path}_{i + 1}"  # Replicate the path with a unique identifier
            new_path_details = {}

            # Update operationId for each method (get, post, etc.)
            for method, method_details in details.items():
                new_method_details = method_details.copy()
                if 'operationId' in new_method_details:
                    new_operation_id = f"{new_method_details['operationId']}_{i + 1}"
                    new_method_details['operationId'] = new_operation_id
                new_path_details[method] = new_method_details

            new_paths[new_path] = new_path_details  # Assign updated details to the new path

    # Update swagger data with new paths
    swagger_data['paths'] = new_paths

    # Write the updated swagger to a new file
    with open(output_path, 'w') as file:
        yaml.dump(swagger_data, file, default_flow_style=False)

    print(f"Swagger file with {num_replicas} replicas per path saved to {output_path}")

# Usage
generate_replicas('swagger.yml', 'swagger_replicated.yml')
