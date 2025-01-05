#!/bin/bash
# Script builds containers and tests them
# Using image already built in containers/ directory
# Have env vars ready in your env..Mine are stored in ~/secrets/home-aap-env-vars
# Run: $ app/tests/container.sh


podman_image=localhost/my-python-project-image:latest
container_root_name=test-container
# git_repo_dir=query-countries-data

link_1=http://192.168.1.100:5000/countries/Kenya
link_2=http://192.168.1.100:5000/countries/Wakanda
link_3=http://192.168.1.100:5000/countries/all

source ~/secrets/home-aap-env-vars

build_container(){
    echo "" && echo "==> Building 3 podman containers" && echo ""

    for i in {1..3}; do
      echo "" && echo "Starting container $container_root_name-$i..."
      podman run -d --name $container_root_name-$i $podman_image sleep infinity
    done

    # Give containers a few seconds to initialize
    sleep 5
}


run_curl(){

    # Running curl to simulate client's requests
    
    echo "" && echo "==> Testing API endpoint " && echo ""
    
    # suppress the progress bar (% Total % Received), you can use the -s (silent) option in curl.
    for i in {1..3}; do
        echo "" && echo ">>> Running curl command in $container_root_name-$i..."
        podman exec $container_root_name-$i curl -s $link_1 && echo
        podman exec $container_root_name-$i curl -s $link_2 && echo
        podman exec $container_root_name-$i curl -s $link_3 && echo
    done
}

# Incase I want to clone stuff and test
clone_and_test(){
    
    # But clients need to have own repo that has ONLY client modules!!
    # test client.py
    for i in {1..3}; do
       echo "" && echo "Cloning repository into $container_root_name-$i..."
       podman exec $container_root_name-$i git clone https://$GITHUB_USER:$GITHUB_ACCESS_TOKEN@github.com/$GITHUB_USER/query-countries-data.git
       podman exec $container_root_name-$i ls -al && echo
       podman exec $container_root_name-$i ls -al query-countries-data && echo
       podman exec $container_root_name-$i python3 query-countries-data/app/tests/test-client.py && echo
       # Kept getting error : 'Error: executable file `cd` not found in $PATH: No such file or directory'

       # Change working directory instead.

    done
}


kill_container(){

    echo "" && echo "==> Killing the containers"

    for i in {1..3}; do
       echo "" && echo ">>> Stopping and removing $container_root_name-$i..."
       podman stop $container_root_name-$i
       podman rm $container_root_name-$i
    done

    echo "" && echo "==> All containers stopped and removed."
}

build_container
clone_and_test
run_curl
kill_container