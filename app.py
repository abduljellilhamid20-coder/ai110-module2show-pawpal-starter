import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.caption("A smart pet care planning assistant.")

# Initialize session state
if "owner" not in st.session_state:
    st.session_state.owner = None

if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

# Step 1: Owner setup
st.subheader("👤 Owner Info")
owner_name = st.text_input("Your name", value="Abduljellil")

if st.button("Set Owner"):
    st.session_state.owner = Owner(name=owner_name)
    st.session_state.scheduler = Scheduler(st.session_state.owner)
    st.success(f"Welcome, {owner_name}!")

st.divider()

# Step 2: Add a pet
st.subheader("🐾 Add a Pet")
col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name", value="Biscuit")
with col2:
    pet_breed = st.text_input("Breed", value="Golden Retriever")

if st.button("Add Pet"):
    if st.session_state.owner is None:
        st.error("Please set your name first!")
    else:
        new_pet = Pet(name=pet_name, breed=pet_breed)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"Added {pet_name} the {pet_breed}!")

st.divider()

# Step 3: Add a task
st.subheader("📋 Add a Task")
if st.session_state.owner and st.session_state.owner.pets:
    pet_options = [p.name for p in st.session_state.owner.pets]
    selected_pet = st.selectbox("Select pet", pet_options)

    col1, col2 = st.columns(2)
    with col1:
        task_desc = st.text_input("Task description", value="Morning walk")
        task_time = st.text_input("Time (HH:MM)", value="08:00")
        task_duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=30)
    with col2:
        task_priority = st.selectbox("Priority", ["high", "medium", "low"])
        task_frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add Task"):
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet:
                pet.add_task(Task(
                    description=task_desc,
                    time=task_time,
                    duration=task_duration,
                    priority=task_priority,
                    frequency=task_frequency
                ))
                st.success(f"Added '{task_desc}' to {selected_pet}!")
else:
    st.info("Add a pet first to start scheduling tasks.")

st.divider()

# Step 4: View schedule
st.subheader("📅 Today's Schedule")
if st.button("Generate Schedule"):
    if st.session_state.scheduler is None:
        st.error("Please set your name first!")
    else:
        schedule = st.session_state.scheduler.get_todays_schedule()
        if not schedule:
            st.info("No tasks yet!")
        else:
            for pet_name, task in schedule:
                status = "✅" if task.completed else "⬜"
                st.markdown(
                    f"{status} **{task.time}** — {task.description} "
                    f"({pet_name}) [{task.priority}] {task.duration}min"
                )

        # Show conflicts
        conflicts = st.session_state.scheduler.detect_conflicts()
        if conflicts:
            st.divider()
            for c in conflicts:
                st.warning(c)
        else:
            st.success("No conflicts found!")