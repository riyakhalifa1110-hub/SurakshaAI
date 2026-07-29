const statCounters = document.querySelectorAll(".stat-number");

const speed = 150;

statcounters.forEach(counter => {

    const update = () => {

        const target = +counter.getAttribute("data-target");

        const count = +counter.innerText;

        const increment = target / speed;

        if (count < target) {

            counter.innerText = Math.ceil(count + increment);

            setTimeout(update, 15);

        } else {

            if (target >= 1000) {
                counter.innerText = (target / 1000) + "K+";
            }
            else if (target == 99) {
                counter.innerText = "99%";
            }
            else {
                counter.innerText = target;
            }

        }

    };

    update();

});



const counters=document.querySelectorAll(".stat-number");

counters.forEach(counter=>{

const update=()=>{

const target=+counter.getAttribute("data-target");

const count=+counter.innerText;

const speed=80;

const increment=Math.ceil(target/speed);

if(count<target){

counter.innerText=count+increment;

setTimeout(update,20);

}else{

counter.innerText=target;

}

}

update();

});