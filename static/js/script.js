// JavaScript to handle complaints form submission
document.addEventListener("DOMContentLoaded", () => {
    const complaintForm = document.getElementById("complaintForm");
    const complaintsList = document.getElementById("complaintsList");

    complaintForm.addEventListener("submit", (event) => {
        event.preventDefault();

        // Get form input values
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const complaint = document.getElementById("complaint").value;

        // Create a new list item to display the complaint
        const listItem = document.createElement("li");
        listItem.innerHTML = `<strong>${name}</strong> (${email}): ${complaint}`;

        // Append the complaint to the complaintsList
        complaintsList.appendChild(listItem);

        // Clear the form input fields
        complaintForm.reset();
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const eventList = document.getElementById("event-list");

    const events = [
        {
            title: "Chess Competition",
            banner: "chess-banner.jpg",
            date: "Monday, August 16",
            location: "Community Center",
            time: "3:00 PM - 6:00 PM",
            description: "Join us for an exciting chess competition!"
        },
        // Add more event objects here
         {
             title: "Acoustic Night",
             banner: "event2.jpg",
             date: "Wednesday, August 18",
             location: "Society-Hall",
             time: "4:00 PM - 8:00 PM",
             description: "The popular singer 'Swopna Suman' will be joining us. It's gonna be so much fun. Hope to see you all there."
         },
         {
            title: "Teej Program",
            banner: "event3.jpg",
            date: "Saturday,August 21",
            location: "Society-Garden",
            time: "1:00 AM - 6:00 PM",
            description: " There will be a singing, dancing programs. People can show whatever talent they have like drama, dance etc. The program will formally ends after having 'Daar'. "
        },
    
    ];

    events.forEach((event, index) => {
        const eventDiv = document.createElement("div");
        eventDiv.classList.add("event");

        eventDiv.innerHTML = `
            <h2>${index + 1}. ${event.title}</h2>
            <img src="${event.banner}" alt="${event.title}">
            <p><strong>Date:</strong> ${event.date}</p>
            <p><strong>Location:</strong> ${event.location}</p>
            <p><strong>Time:</strong> ${event.time}</p>
            <p>${event.description}</p>
        `;

        eventList.appendChild(eventDiv);

        // Add gaps between events
        if (index < events.length - 1) {
            const eventGap = document.createElement("div");
            eventGap.classList.add("event-gap");
            eventList.appendChild(eventGap);
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const addMemberForm = document.getElementById("addMemberForm");
    const coreMemberProfiles = document.getElementById("core-member-profiles");

    // Function to create a member profile
    function createMemberProfile(member) {
        const profileDiv = document.createElement("div");
        profileDiv.classList.add("core-member-profile");
        profileDiv.innerHTML = `
            <img src="${member.photo}" alt="${member.name} Photo" class="core-member-photo">
            <div class="core-member-info">
                <h3 class="core-member-name">${member.name}</h3>
                <p class="core-member-title">${member.title}</p>
                <p class="core-member-description">${member.description}</p>
                <p class="core-member-contact">Email: ${member.email}</p>
                <p class="core-member-contact">Phone: ${member.phone}</p>
            </div>
        `;
        return profileDiv;
    }

    // Sample core member data
    const coreMembers = [
        {
            name: "Sujana Acharya",
            title: "President",
            description : "She is an energetic, enthusiastic person, serving this society being president since 2015.",
            email: "sujanaacharya@.com",
            phone: "9852647852",
            photo: "president.jpg"
        },
        {
            name: "Prasamsha Dotel",
            title: "Vice President",
            description: "She is a kind, enthusiastic person, serving this society as vice-president since 2015.",
            email: "prasamsha5555@.com",
            phone: "9860062092",
            photo: "vicepresident.jpg"
        },
        // Add other core members here
        {
            name: "Apsara Shrestha",
            title: "Secretary",
            description: "She is a smart,joyous person, serving this society as a Secretary since 2015.",
            email: "prasamsha5555@.com",
            phone: "9845864092",
            photo: "secretary.jpg"
        },
    ];

    // Function to dynamically generate core member profiles
    function generateCoreMemberProfiles() {
        coreMembers.forEach(coreMember => {
            const profileDiv = createMemberProfile(coreMember);
            profileDiv.classList.add("core-member-profile");
            coreMemberProfiles.appendChild(profileDiv);
        });
    }

    // Call the function to generate core member profiles
    generateCoreMemberProfiles();

    // Handle form submission for adding new members
    addMemberForm.addEventListener("submit", (event) => {
        event.preventDefault();

        // Get form input values (assuming your form has fields with IDs "name", "title", "description", etc.)
        const name = document.getElementById("name").value;
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;
        const email = document.getElementById("email").value;
        const phone = document.getElementById("phone").value;
        const photo = "default-photo.jpg"; // Replace with the actual file path of the photo

        // Create a new core member object
        const newCoreMember = {
            name: name,
            title: title,
            description: description,
            email: email,
            phone: phone,
            photo: photo
        };

        // Create and append the new core member profile
        const newProfileDiv = createMemberProfile(newCoreMember);
        newProfileDiv.classList.add("core-member-profile");
        coreMemberProfiles.appendChild(newProfileDiv);

        // Clear the form input fields
        addMemberForm.reset();
    });

    // ... (rest of your code)
});
