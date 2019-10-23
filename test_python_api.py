import ec2_cluster
from ec2_cluster.infra import ConfigCluster
from ec2_cluster.control import ClusterShell





def get_test_cluster():
    print("ec2-cluster version:", ec2_cluster.__version__)
    cluster = ConfigCluster(config_yaml_path="test_config.yaml")

    if not cluster.any_node_is_running_or_pending():
        cluster.launch(verbose=True)

    print("Cluster id:", cluster.cluster_name)
    return cluster





if __name__ == '__main__':
    cluster = get_test_cluster()
    sh = ClusterShell.from_ec2_cluster(cluster, ssh_key_path="~/.ssh/ec2-cluster-test.pem")

    print("hidden output ---")
    sh.run_on_all("hostname", hide=True)
    print("---")
    results = sh.run_on_all("ls /")
    print("----")
    print(results)

    cluster.terminate(verbose=True)


